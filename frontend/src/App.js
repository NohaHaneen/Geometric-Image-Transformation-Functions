import React from 'react';
import { Container } from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.css";
import {InputNoImageCard,InputImageCard,OutputNoImageCard,OutputImageCard} from './components/Card';
import Button from '@mui/material/Button';
import UploadIcon from '@mui/icons-material/FileUploadOutlined';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import TextField from '@mui/material/TextField';
const axios = require('axios');

const transformations = [
  {
    value: 'Scaling',
    label: 'Scaling',
  },
  {
    value: 'Translation',
    label: 'Translation',
  },
  {
    value: 'Rotation',
    label: 'Rotation',
  },
  {
    value: 'Affine',
    label: 'Affine',
  },
  {
    value: 'Perspective',
    label: 'Perspective',
  },
  {
    value: 'Polar',
    label: 'Polar',
  },
  {
    value: 'LogPolar',
    label: 'LogPolar',
  },
];

function App() {
  const [transformationOperation, setTransformationOperation] = React.useState('Scaling')
  const [parameterValues, setParameterValues] = React.useState('')
  const [inputImageName, setInputImageName] = React.useState('')
  const [inputImage, setInputImage] = React.useState('')
  const [outputImage, setOutputImage] = React.useState('')
  const [isLoading, setIsLoading] = React.useState(false)

  const handleDropDownChange = (event) => {
    setTransformationOperation(event.target.value);
  }

  const handleParameter = (event) => {
    setParameterValues(event.target.value)
  }

  const fileUpload = (event) => {
    console.log(event.target.files)
    if(event.target.files['length'] > 0){
      // file is present
      let data = new FormData();
      data.append('file', event.target.files[0]);
      setInputImageName(event.target.files[0].name)
      axios.post('/upload', data)
        .then((response) => {
          console.log(response);
          setInputImage(response.data)
        })
        .catch(function (error) {
          console.log(error);
        });
    }else{
      //file is not present
      setInputImage('')
    }
  }

  const onClickClear = () => {
    // console.log("clear clicked")
    // setInputImage('')
    // setOutputImage('')
    window.location.reload()
  }

  const onClickSubmit = () => {
    let request = {
      inputImageName : inputImageName,
      parameters : parameterValues,
      transformation : transformationOperation
    }

    setIsLoading(true)
    axios.post('/submit', request)
      .then((response) => {
        console.log(response);
        setOutputImage(response.data)
        setIsLoading(false)
      })
      .catch(function (error) {
        console.log(error);
        setIsLoading(false)
      });
  }

  return (
    <Container
      style={{ minHeight: "100vh", paddingLeft: '0', paddingRight: '0',background:'#EEEEEE',overflow:'hidden' }}
      fluid
    > 
      <br/>
      <div className={"row"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
        <h1 style={{color:'#1976d2'}}>Image Geometric Transformation</h1>
      </div>
      <br/>
      <div className={"row"}>
        <div className={"col-sm-6"} >
          <div className={"row"} >
            <div className={"col-sm-12"} style={{fontSize:'24px',display:'flex',justifyContent:'center',alignItems:'center'}}>
              Input
            </div>
            <div className={"col-sm-12"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
               {/* display image */}
               {inputImage && (
                 <InputImageCard imageURL={inputImage}/>
               )}

               {/* display no image */}
               {!inputImage && (
                 <InputNoImageCard />
               )}
            </div>
          </div>
        </div>
        <div className={"col-sm-6"}>
          <div className={"row"} >
            <div className={"col-sm-12"} style={{fontSize:'24px',display:'flex',justifyContent:'center',alignItems:'center'}}>
              Output
            </div>
            <div className={"col-sm-12"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
              {/* display image */}
              {outputImage && (
                 <OutputImageCard imageURL={outputImage}/>
               )}

               {/* display no image */}
               {!outputImage && (
                 <OutputNoImageCard isLoading={isLoading}/>
               )}
            </div>
          </div>
        </div>
      </div>
      <br/>

      <div className={"row"}>
        <div className={"col-sm-4"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
          <Button
            variant="contained"
            component="label"
            startIcon={<UploadIcon />}
            
          >
            Upload File
            <input
              type="file"
              hidden
              onChange={(event)=> { 
                fileUpload(event) 
              }}
            />
          </Button>
        </div>
        <div className={"col-sm-4"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
          <FormControl sx={{ m: 0, width: 300, mt: 3 }}>
            <TextField
              id="outlined-select-currency"
              select
              label="Choose Transformation"
              value={transformationOperation}
              onChange={handleDropDownChange}
            >
              {transformations.map((option) => (
                <MenuItem key={option.value} value={option.value}>
                  {option.label}
                </MenuItem>
              ))}
            </TextField>
          </FormControl>
        </div>
        <div className={"col-sm-4"} style={{display:'flex',justifyContent:'center',alignItems:'center'}}>
          <FormControl sx={{ m: 0, width: 300, mt: 3 }}>
            <TextField 
              fullWidth 
              label="Enter Parameters" 
              id="Parameters" 
              value={parameterValues}
              onChange={handleParameter}
            />
          </FormControl>
        </div>
      </div>
      <br />
      <br />
      <div className={"row"}>
        <div className={"col-sm-12"} style={{display:'flex',justifyContent:'flex-end',alignItems:'center',paddingRight:'7%'}}>
          <div style={{paddingRight:'2%'}}>
            <Button variant="outlined" onClick={onClickClear}>Clear</Button>
          </div>
          <div>
            <Button variant="contained" onClick={onClickSubmit}>
              Submit
            </Button>
          </div>
        </div>
      </div>
    </Container>
  )
}

export default App;