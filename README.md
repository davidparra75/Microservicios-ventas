# Microservicios-ventas
# Sistema de Microservicios

## 1. Arquitectura del sistema
El sistema se diseñó siguiendo una arquitectura de microservicios, donde cada servicio tiene una responsabilidad específica y se comunica a través de un API Gateway desarrollado en Laravel.

El Gateway centraliza las peticiones del cliente, valida la autenticación mediante JWT y coordina la comunicación entre los microservicios.

### Componentes del sistema

**API Gateway (Laravel)**
- Gestiona autenticación con JWT.
- Recibe las solicitudes del cliente.
- Orquesta la comunicación entre microservicios.

**Microservicio de Inventario (Flask)**
- Desarrollado con Flask.
- Permite consultar productos disponibles.
- Permite actualizar el stock después de una venta.
- Utiliza Firebase para almacenamiento.

**Microservicio de Ventas (Express)**
- Desarrollado con Express.js.
- Permite registrar ventas.
- Permite consultar ventas registradas.
- Utiliza MongoDB para almacenamiento.

---

## 2. Endpoints disponibles a través del Gateway

Todos los endpoints deben ser consumidos desde el **API Gateway**, el cual se encarga de redirigir la solicitud al microservicio correspondiente.

### Autenticación

| Método | Endpoint       | Descripción        |
|--------|----------------|--------------------|
| POST   | /api/register  | Registrar usuario  |
| POST   | /api/login     | Iniciar sesión     |
| POST   | /api/logout    | Cerrar sesión      |

### Ventas

| Método | Endpoint                | Descripción                  |
|--------|-------------------------|------------------------------|
| POST   | /api/sales              | Registrar una venta          |
| GET    | /api/sales              | Consultar todas las ventas   |
| GET    | /api/sales/user/{id}    | Consultar ventas por usuario |
| GET    | /api/sales/date/{date}  | Consultar ventas por fecha   |

---

## 3. Flujo de registro de una venta

El proceso de registro de una venta sigue los siguientes pasos:

1. El cliente envía una solicitud al API Gateway para registrar una venta.
2. El Gateway valida la autenticación del usuario mediante JWT.
3. El Gateway consulta el microservicio de inventario para verificar la disponibilidad del producto.
4. Si el producto tiene stock disponible, el Gateway envía la solicitud al microservicio de ventas.
5. El microservicio de ventas registra la venta en la base de datos MongoDB.
6. El Gateway solicita al microservicio de inventario actualizar el stock del producto.
7. Finalmente, el sistema devuelve la respuesta al cliente confirmando la venta.
