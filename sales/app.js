require("dotenv").config()

const express = require("express")
const cors = require("cors")

const connectDB = require("./config/db")
const salesRoutes = require("./routes/salesRoutes")
const app = express()
connectDB()

app.use(cors())
app.use(express.json())

app.use("/sales",salesRoutes)
const PORT = process.env.PORT || 3002

app.listen(PORT, () =>  {
    console.log(`microservicio de ventas corriendo en puerto ${PORT}`)
})
