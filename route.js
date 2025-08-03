const app=require('../app')
const modelcontroller=require('../Controllers/modelcontroller')
const express=require('express')
const router=express.Router()

router.route('/traindata').get(modelcontroller.getTraindata).post(modelcontroller.createdata)
router.route('/predictdata').post(modelcontroller.createpredictdata)
//router.route('/:id').patch(modelcontroller.updateData).delete(modelcontroller.deleteData)
module.exports=router;