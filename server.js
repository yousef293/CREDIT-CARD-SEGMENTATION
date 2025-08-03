const dotenv=require('dotenv');
const app = require('./app')
const mongoose = require('mongoose');
dotenv.config({ path: './config.env' });
mongoose.connect(process.env.DBURL,{useNewUrlParser:true}).then(()=>console.log('server is connected to database'))
.catch(err=>console.log('Error connecting to database:'+ err));

app.listen(process.env.PORT,()=>console.log(`Server is running on port ${process.env.PORT}`));
