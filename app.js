const express=require('express');
const mongoose=require('mongoose');
const datarouter=require('./Routes/route')
const app= express();

app.use(express.json());
app.use((req,res,next)=>{req.requestTime=new Date().toISOString();
    console.log("Success"+req.requestTime);
    next()
})


app.use(datarouter)



module.exports=app;