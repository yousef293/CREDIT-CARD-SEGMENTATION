
const { Segment, Predict } = require('../Model/vehicleModels');

const fs =require('fs')

//Get
exports.getTraindata = async function(req,res) {
    try{
     const segment=await Segment.find()
    res.status(200).json({
        data:segment
    })
}catch(err){res.status(400).json({
    status:'failed',
    message:err
})}
}
//Create
const datafile=JSON.parse(fs.readFileSync('./converted_data.json','utf-8'))
exports.createdata=async function(req,res){
    try{
        //const Batch_size=20;
        //for(let i=0;i<datafile.length;i+=Batch_size){
            //let chunk=datafile.slice(i,i+Batch_size)
            await Segment.insertMany(datafile)
    res.status(201).json({
        status:'success',
    })}catch(err){res.status(400).json({
        status:"failed",
        message:err
    })}


}
exports.createpredictdata=async function(req,res){
        try{
       
        await Predict.insertMany(req.body)
    res.status(201).json({
        status:'success',
    })}catch(err){res.status(400).json({
        status:"failed",
        message:err.message
    })}
}








/*
//Update

exports.updateData=async function(req,res){
    try{
        const updatedVehicle=await Vehicle.findByIdAndUpdate(req.params.id,req.body,{new:true ,runvalidators:true})
        res.status(200).json({
            status:"success",
            data:updatedVehicle
        })
    }
catch(err){res.status(404).json({
    status:"failed",
    message: err
})

}}

//delete
exports.deleteData=async function(req,res){
    try{
        const deletedVehicle=await Vehicle.findByIdAndDelete(req.params.id)
        res.status(204).json({
            status:"success",
            message:`the data with the id ${req.params.id} deleted successfully` 
        })
    }catch(err){res.status(404).json({
        status:"failed",
        message:err
    })}
}*/