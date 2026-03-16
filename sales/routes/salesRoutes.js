const express = require("express")
const router = express.Router()

const {
    createSale,
    getSales,
    getSalesByUser,
    getSalesByDate
} = require("../controllers/SalesController")

router.post("/",createSale)
router.get("/",getSales)
router.get("/user/:user",getSalesByUser)
router.get("/date/:date",getSalesByDate)

module.exports = router
