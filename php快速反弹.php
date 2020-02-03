<?php
function send_post($url, $post_data)
{
    $postdata = http_build_query($post_data);
    $options = array(
        'http' => array(
            'method' => 'POST',
            'header' => 'Content-type:application/x-www-form-urlencoded',
            'content' => $postdata,
        )
    );
    $context = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    echo $result;  //输出post请求后页面内容
}
/**********************调用方式************************/
/*$post_data = array(
    'token' => $token
);
send_post('http://9b7ea44499.php.hgame.n3ko.co/', $post_data);*/
/*********************调用方式************************/

/*********************获取页面指定内容一般方式************************/
/*$url="http://11fd5a58f8.php.hgame.n3ko.co";
$token=file_get_contents($url);     //获取页面内容
$token=explode("\n", $token);       //把获取的内容按换行符分成数组
$token=$token[4];       //取数组第四个元素*/
/*********************获取页面指定内容一般方式************************/






