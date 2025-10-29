# 🪙 Python Minimal Blockchain (PoW) 🐍

Una **implementación educativa y funcional** de una cadena de bloques básica utilizando Python. Este proyecto se enfoca en demostrar los conceptos centrales de la criptografía, la inmutabilidad y el algoritmo de **Prueba de Trabajo** (Proof-of-Work, PoW).

Ideal para desarrolladores que desean entender los **fundamentos** de tecnologías descentralizadas (Web3) o como una herramienta para practicar conceptos de algoritmos y seguridad.

---

## 🚀 Características Clave

* **Bloques Criptográficamente Enlazados:** Implementación de la clase `Block` para asegurar la inmutabilidad de los datos mediante *hashing* **SHA-256**.
* **Prueba de Trabajo (PoW):** Algoritmo de minería funcional que ajusta la dificultad (actualmente, buscar un *hash* que comience con **`0000`**).
* **Gestión de Transacciones:** Maneja transacciones pendientes antes de ser empaquetadas en un nuevo bloque.
* **Validación de Cadena:** Incluye una función (`is_chain_valid`) para verificar la integridad de toda la cadena, demostrando la **inmutabilidad** de la *blockchain*.
* **Lenguaje:** 100% **Python**.

---

## 🛠️ Requisitos e Instalación

Este proyecto es extremadamente ligero. Solo requiere Python 3.x y las bibliotecas estándar.

### Requisitos

* Python 3.6 o superior.

### Ejecución

1.  Guarda el código completo proporcionado en un archivo llamado `simple_blockchain.py`.
2.  Ejecuta el archivo desde tu terminal:

    ```bash
    python simple_blockchain.py
    ```

    Verás cómo se inicializa el **Bloque Génesis**, se añaden transacciones, se ejecuta el proceso de **minería (PoW)** y finalmente se valida la cadena.

---

## 🧠 Estructura del Código

El proyecto consta de dos clases principales:

| Clase | Responsabilidad |
| :--- | :--- |
| **`Block`** | Define la estructura de cada unidad de datos. Contiene el índice, *timestamp*, datos, *previous\_hash* y el *nonce* (resultado de la minería). |
| **`Blockchain`** | Gestiona la cadena (`self.chain`), las transacciones pendientes (`self.pending_transactions`) y contiene la lógica para la **minería** y la **validación**. |

---

## 💡 Próximos Pasos (Contribuciones)

Este es un proyecto base excelente. Si quieres contribuir o expandir tu portafolio, considera añadir:

* **API Web (con Flask o FastAPI):** Conviértelo en una red de nodos real implementando *endpoints* para añadir transacciones, minar y resolver conflictos (regla de consenso).
* **Firmas Digitales (Criptografía Real):** Usa el módulo `ecdsa` o `cryptography` de Python para que las transacciones sean firmadas por el emisor.
* **Persistencia de Datos:** Almacena la cadena en un archivo JSON o una base de datos real en lugar de mantenerla solo en memoria.

---

## 👤 Autor

Desarrollado por [siforiano]

* **GitHub:** [@siforiano](https://github.com/siforiano)
