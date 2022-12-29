<?php
    //p2.php
    include  "bn.html";
?>
<h1>โปรแกรมคำนวณหาค่า BMI v2</h1>
<form action="" method="post">
    ชื่อ : <input type="text" name="name"><br>
    น้ำหนัก: <input type="text" name="weight"><br>
    ความสูง: <input type="text" name="height"><br>
    <input type="submit">
</form>

 <?php
 //รับค่าจากฟอร์มและแสดงผลโดยให้ตรวจสอบค่า
 if(isset($_POST['name'])){
 $bmi = $weight / pow(($height/100),2);
 echo "ข้อมูลของคุณ " . $name . "<br>";
 echo "BMI = " . number_format($bmi,2) . "<br>";
 
  //นำค่า BMI ไปตรวจสอบตามเงื่อนไข
 if ($bmi < 18.50){
     echo "คุณเป็นคน : น้ำหนักต่ำเกณฑ์";
 } elseif ($bmi >= 18.51 and $bmi <= 22.99){
    echo "คุณเป็นคน : สมส่วน";
 } elseif ($bmi >= 23 and $bmi <= 24.99){
    echo "คุณเป็นคน : น้ำหนักเกิน";
 }elseif ($bmi >= 25 and $bmi <= 29.99){
    echo "คุณเป็นคน : โรคอ้วน";
 }else echo "คุณเป็นคน : โรคอ้วนอันตราย";
}
 ?>