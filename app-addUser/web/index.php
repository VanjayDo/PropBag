<html>
<head>
    <title>index</title>
    <meta charset="UTF-8">
</head>

<h3>添加一个用户</h3>
<form id="addUser" action="index.php" method="post">
    用户名: <input type="text" name="username"><br>
    密 码:<input type="password" name="pwd">
    <input type="submit">
</form>
</body>
</html>

<?php
function curlAdd($username, $pwd)
{
    if ($username && $pwd) {
        $url = "http://localhost:8080/UserController/add";
        $post_data = array(
            "username" => $username,
            "pwd" => $pwd
        );
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        $response = curl_exec($ch);
        curl_close($ch);
        if (strstr($response, "success")) {
            echo "<script>alert('添加成功');</script>";
        } else {
            echo "<script>alert('添加失败');</script>";
        }
    } else {
        echo "<script>alert('请填写正确的用户名密码');</script>";
    }
}

function curlList()
{
    echo "<div align='center'><h3>=====this is the list of users=====</h3>";
    $url = "http://localhost:8080/UserController/list";

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 0);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}


if (@$_POST["username"] && @$_POST["pwd"]) {
    curlAdd($_POST["username"], $_POST["pwd"]);
}

$result = json_decode(curlList());
echo "<table border='1'>
  <tr>
    <th>id</th>
    <th>username</th>
    <th>pwd</th>
  </tr>
";
if($result)
{
    foreach ($result as $item) {
        echo "<tr>";
        foreach ($item as $value) {
            echo "<td>";
            echo $value;
            echo "</td>";
        }
        echo "</tr>";
    }
}

echo "</table></div>";