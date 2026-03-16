<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class SalesController extends Controller
{
    public function registerSale(Request $request){
       $productId=$request->product_id;
       $quantity=$request->quantity;

       // Consultar inventario en flask
       $inventory = Http::get("http://localhost:5000/products/$productId");

       if (!$inventory -> successful()){
        return response()->json(['error'=>'Error consultando inventario'],500);
       }
       
       $stock = $inventory->json()['stock'];

       // 2 verifica stock
       if ($stock < $quantity){
        return response()->json(['error'=>'Cantidad en stock insuficiente'],400);
       }
       
       //3 venta en express
       $sale = Http::post("http://localhost:3000/sales",[
           'product_id'=>$productId,
           'quantity'=>$quantity,
           'user_id'=>auth()->user()->id
        ]);

        //4 actualizar inventario flask
        Http::put("http://localhost:5000/products/$productId",[
            'quantity'=>$quantity
        ]);
        return response()->json($sale->json());
    }
}
