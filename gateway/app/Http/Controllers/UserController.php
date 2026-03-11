<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Tymon\JWTAuth\Facades\JWTAuth;

class UserController extends Controller
{
    public function register(Request $request){
        $user = new User;
        $user->name = $request->name;
        $user->email = $request->email;
        $user->password = bcrypt($request->password);
        $user->save();
        return response()->json(['message'=>'Usuario registrado']);
        
    }

    public function login(Request $request){
        $credentials = $request->only('email','password');

        if(!$token = JWTAuth::attempt($credentials)){
            return response()->json(['message'=>'credenciales invalidas'],401);
        }
        return response()->json(['access_token'=>$token, 'token_type'=> 'Bearer']);
    }

    public function logout(Request $request){
        JWTAuth::parseToken()->invalidate();
        return response()->json([
        'message'=>'Sesión cerrada'
        ]);
    }
}
