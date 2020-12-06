// ==UserScript==
// @name         test2
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       AnAn
// @match        http://202.117.144.205:*/snnuportal/login.jsp
// @match        http://202.117.144.205:*/snnuportal/logoff
// @connect      *
// @grant        GM_xmlhttpRequest
// @require      http://202.117.144.205:8601/snnuportal/js/jquery-1.4.4.js
// ==/UserScript==



(function() {
    'use strict';
    $.noConflict();
    var i=0;
    var ip_element=document.querySelector("body > form > blockquote > table:nth-child(1) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > span");
    var ip=ip_element.innerHTML.match(/当前IP:(.*) /)[1];
    var re=/<td bgcolor="#FFFFFF"><iframe align="middle" frameborder="0" width="100%" height="200" scrolling="yes" src="(.*?)"/m;
    var root=document.location.href.match(/http:\/\/202.117.144.205:[0-9]*\/snnuportal\//);
    function denglu(account,password) {
        jQuery("#alert_span").text(++i);
        if(i>180){
            alert("测试次数大于上限，测试失败");
            return;
        }
        jQuery.ajax({
            url: root+'bind',
            type:"post",
            dataType:"json",
            data:{
                account:account,
                password:password,
                method: 'getUserInfo'
            },
            success:function(resp){
                jQuery.ajax({
                    url:root+'login',
                    type:"post",
                    dataType:"html",
                    data:{
                        sourceurl: 'null',
                        account: account,
                        password: password,
                        yys: '',
                        issave: ''
                    },
                    success:function(resp) {
                        if(resp.search("登录失败")>=0){
                            alert("密码或者账号错误");
                            return;
                        }
                        if(resp.search("Juniper")>=0){
                            alert("需要更换当前ip，请更换ip(更换mac地址即可更换ip)");
                            document.location.assign(root+"userstatus.jsp");
                        }
                        var t_url=resp.match(re)[1];
                        GM_xmlhttpRequest({
                            method:"GET",
                            url:t_url,
                            type:"get",
                            onload:function (resp) {
                                if(resp.responseText.search(ip)>=0){
                                    jQuery.ajax({
                                        url:root+'logoff',
                                        type:"get",
                                        dataType:"html",
                                        success:function(){
                                            denglu(account,password);
                                        }

                                    });


                                }else{
                                    alert("测试成功");
                                    document.location.assign(root+"userstatus.jsp");
                                }
                            }
                        });

                    }
                })}});}
    function test(){
        var account = document.forms[0].account.value;
        account = jQuery.trim(account);
        if (!account) {
            alert("账户名空");
            return;
        }
        var password = document.forms[0].password.value;
        password = jQuery.trim(password);
        if (!password) {
            alert("密码空");
            return;
        }
        denglu(account,password);
    }
    window.setTimeout(function(){
        var ss=jQuery("a[onclick='loginSubmit(false);']");
        ss.removeAttr("onclick");
        ss.removeAttr("href");
        ss.attr("id","nima");
        jQuery("body:first").append("<div id='alert_div'>测试进度：<span id='alert_span'>0</span></div>");
        jQuery("#alert_div").attr({"style":"position:relative;text-align:center;margin:auto;font-size:2rem"});
        document.getElementById("nima").addEventListener("click",test,false);
    }, 60);


})();