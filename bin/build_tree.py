#!/usr/bin/env python3
"""
Institutional-tree graph demo.

Builds the Node graph from a list of institutional codes and renders it
to an image with networkx/matplotlib.

Moved from scripts/tree.py. Differences from the original:
- Import-safe: nothing runs at import time (the original built the graph
  and wrote graph.png on import).
- argparse CLI: --paths-file (one code per line) or --code CODE ...
  instead of a hardcoded list; --out for the image path; --print-nodes.
- The `up()` no-op limitation is kept but now warns explicitly instead of
  silently dropping shorter codes.

Usage:
    python3 bin/build_tree.py --out graph.png
    python3 bin/build_tree.py --paths-file codes.txt --out data/tree.png --print-nodes
"""

import argparse
import collections
import sys
from pathlib import Path

DEFAULT_PATHS = [
    "00",
    "01",
    "0101",
    "01",
    "0001",
    "0102",
    "01",
    "0001",
    "02",  # Poder Ejecutivo
    "0201",
    "01",
]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.down = None
        self.up = None

    def __repr__(self):
        return f"Node({self.value})"


def build_graph(paths):
    if not paths:
        raise ValueError(
            "Error: The 'paths' list should not be empty. "
            "Please ensure that it contains elements."
        )
    main = Node(paths[0])

    for item in paths[1:]:
        node = Node(item)
        add_node(node, main)

    return main


def add_node(node, graph):
    """
    Attach node to the graph.

    NOTE (carried over from the original): shorter codes hit the `up`
    branch, which is a no-op — such nodes are created but left detached.
    A warning is emitted so this is not silent.

    Map:
         -> Node -> down, right, up(n level)
         -> Place The Node In That Point

    is len(node) > len(last node) || val(node) > val(last node) -> son
    """

    def down(node, graph):
        graph.down = node
        node.up = graph

    def right(node, graph):
        graph.right = node
        node.left = graph

    def up(node, graph):
        print(
            f"[build_tree] WARNING: code {node.value!r} is shorter than "
            f"{graph.value!r}; up() is a no-op, node left detached.",
            file=sys.stderr,
        )

    if len(node.value) > len(graph.value):
        down(node, graph)
    elif len(node.value) == len(graph.value):
        right(node, graph)
    else:
        up(node, graph)


def traverse(start_node):
    visited = set()
    queue = collections.deque([start_node])
    nodes = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            nodes.append(node)

            # Add adjacent nodes to the queue
            for neighbor in (node.left, node.right, node.up, node.down):
                if neighbor and neighbor not in visited:
                    queue.append(neighbor)

    return nodes


def generate_image(nodes, filename="graph.png"):
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
    except ModuleNotFoundError as exc:
        print(
            f"[build_tree] missing dependency {exc.name}; run `uv sync` "
            "(see pyproject.toml).",
            file=sys.stderr,
        )
        raise SystemExit(2)
    G = nx.DiGraph()

    for node in nodes:
        G.add_node(node.value)
        if node.left:
            G.add_edge(node.value, node.left.value)
        if node.right:
            G.add_edge(node.value, node.right.value)
        if node.up:
            G.add_edge(node.value, node.up.value)
        if node.down:
            G.add_edge(node.value, node.down.value)

    # Create a layout for the nodes
    pos = nx.spring_layout(G)

    # Draw the graph
    plt.figure(figsize=(10, 10))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="skyblue",
        font_size=15,
        font_weight="bold",
    )
    plt.title("Graph Visualization")

    # Save the image
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(filename)
    plt.close()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="build_tree.py")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--paths-file",
        help="File with one institutional code per line.",
    )
    group.add_argument("--code", action="append", help="Institutional code (repeatable).")
    parser.add_argument("--out", default="graph.png", help="Output image path.")
    parser.add_argument(
        "--print-nodes", action="store_true", help="Print traversed nodes to stdout."
    )
    args = parser.parse_args(argv)

    if args.paths_file:
        paths = [
            line.strip()
            for line in Path(args.paths_file).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    elif args.code:
        paths = args.code
    else:
        paths = list(DEFAULT_PATHS)

    if not paths:
        print("[build_tree] ERROR: no codes to graph.", file=sys.stderr)
        return 1

    graph = build_graph(paths)
    nodes = traverse(graph)
    if args.print_nodes:
        print(nodes)
    generate_image(nodes, args.out)
    print(f"[build_tree] wrote {args.out} ({len(nodes)} nodes)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
