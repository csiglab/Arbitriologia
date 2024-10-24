# Descarga de Información de Nóminas

> ...

## Hacer script por cada institucion

**Script**:

- **Input**: Ruta Recursos Humanos, Año
- **Output**: Nomina Mes Enero / SQL Lite. Table
- **Test**:
  - Rutas de Ejemplos
  - ...

**Output Format (SQL Lite)**:

```sql
CREATE TABLE payroll (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incremented primary key
    year INTEGER NOT NULL,                 -- Year of the payroll entry
    month INTEGER NOT NULL,                -- Month of the payroll entry
    name TEXT NOT NULL,                    -- Name of the employee
    organization TEXT NOT NULL,            -- Organization the employee works for
    area TEXT,                             -- Area or department
    role TEXT NOT NULL,                    -- Role of the employee
    salary REAL NOT NULL                   -- Salary of the employee
);
```
