function checkPlagiarism(){

let file1=document.getElementById("file1").files[0]
let file2=document.getElementById("file2").files[0]

if(!file1 || !file2){
alert("Please upload both files")
return
}

let formData=new FormData()

formData.append("file1",file1)
formData.append("file2",file2)

fetch("http://127.0.0.1:5000/check",{
method:"POST",
body:formData
})
.then(response => response.json())
.then(data => {

let result=document.getElementById("result")

result.style.display="block"
result.innerHTML="Plagiarism : "+data.percentage+"%"

if(data.percentage>=30 && data.percentage<=60){
result.style.background="yellow"
result.style.color="black"
}
else{
result.style.background="red"
result.style.color="white"
}

})
.catch(error=>{
console.log(error)
alert("Error connecting to backend")
})

}