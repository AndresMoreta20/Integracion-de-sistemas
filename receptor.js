const Datastore = require("nedb");
const csvParser = require("csv-parser");
const fs = require("fs");

// Crear o abrir una base de datos NeDB
const db = new Datastore({ filename: "salarios.db", autoload: true });

// Salarios base por departamento
const salarios = {
  Analisis: 301.0,
  Desarrollo: 302.0,
  Auditoria: 303.0,
};

// Función para calcular el salario anual
function calcularSalarioAnual(salarioMensual) {
  return salarioMensual * 12.0;
}

// Función para insertar un empleado en la base de datos NeDB si no existe un duplicado
function insertarEmpleadoSiNoExiste(empleado) {
  db.findOne(
    { nombreCompleto: empleado.nombreCompleto, area: empleado.area },
    function (err, doc) {
      if (err) {
        console.error("Error buscando en la base de datos:", err);
        return;
      }
      if (!doc) {
        // Si no se encuentra un documento existente, inserta el nuevo empleado
        db.insert(empleado, function (err, newDoc) {
          if (err) {
            console.error(
              "Error insertando documento en la base de datos:",
              err
            );
            return;
          }
          // Documento insertado con éxito
          console.log("Empleado insertado con éxito:", newDoc);
        });
      } else {
        // Si se encuentra un documento existente, no insertar y posiblemente notificar
        console.log("Empleado duplicado no insertado:", empleado);
      }
    }
  );
}

// Función para leer y procesar el archivo CSV
function importarDatosDesdeCsv() {
  fs.createReadStream("empleados.csv")
    .pipe(csvParser())
    .on("data", (row) => {
      const nombreCompleto = `${row.Nombre} ${row.Apellido}`;
      const area = row.Departamento;

      if (!row.Nombre || !row.Apellido || !row.Departamento) {
        console.error(
          "Uno de los campos está indefinido, revisa los datos:",
          row
        );
        return; // Saltar esta fila si alguno de los campos está indefinido
      }

      // Asignar el salario mensual basado en el área
      const salarioMensual = salarios[area] || 0; // Use 0 or some default if area is not found
      const salarioAnual = calcularSalarioAnual(salarioMensual);

      const empleado = {
        nombreCompleto,
        area, // Usamos 'area' como el nuevo término para 'departamento'
        salarioMensual,
        salarioAnual,
        fechaRegistro: new Date(),
      };
      insertarEmpleadoSiNoExiste(empleado);
    })
    .on("end", () => {
      console.log("Importación de datos CSV completada.");
    });
}

// Ejecutar la importación de datos desde CSV
importarDatosDesdeCsv();
