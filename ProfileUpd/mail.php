<?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        $secretKey = '6Ld42qkZAAAAAKx52n8MyJPPo3R9HMXUBuvCLbez';
        $captcha = $_POST['g-recaptcha-response'];

        if(!$captcha){
            echo ("<script LANGUAGE='JavaScript'>
                    window.alert('Please check the captcha form.')
                    window.location.href='https://ronnda.info';
                </script>
                <NOSCRIPT>
                    <a href='https://ronnda.info'>Please check the captcha form. Click here if you are not redirected.</a>
                </NOSCRIPT>");
          exit;
        }

        $mail_to = "ronnda@zezula.io";
        $subject = "Ronnda.Info Contact";

        #sender info
        $name = str_replace(array("\r","\n"),array(" "," ") , strip_tags(trim($_POST["name"])));
        $phone = trim($_POST["phone"]);
        $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
        $message = trim($_POST["message"]);

        if ( empty($name) OR !filter_var($email, FILTER_VALIDATE_EMAIL) OR empty($message)) {
            #400 (bad request) response code and exit
            http_response_code(400);
            echo ("<script LANGUAGE='JavaScript'>
                    window.alert('Please enter a name, email address, and message then re-submit.')
                    window.location.href='https://ronnda.info';
                </script>
                <NOSCRIPT>
                    <a href='https://ronnda.info'>Please enter a name, email address, and message then re-submit. Click here if you are not redirected.</a>
                </NOSCRIPT>");
            exit;
        }

        $ip = $_SERVER['REMOTE_ADDR'];
        $response=file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=".$secretKey."&response=".$captcha."&remoteip=".$ip);
        $responseKeys = json_decode($response,true);

        if(intval($responseKeys["success"]) !== 1) {
            echo ("<script LANGUAGE='JavaScript'>
                    window.alert('Please check the captcha form.')
                    window.location.href='https://ronnda.info';
                </script>
                <NOSCRIPT>
                    <a href='https://ronnda.info'>Please check the captcha form. Click here if you are not redirected.</a>
                </NOSCRIPT>");
        } else {
            #email content
            $content = "Name: $name\n";
            $content .= "Phone: $phone\n";
            $content .= "Email: $email\n\n";
            $content .= "Message:\n$message\n";

            #email header.
            $headers = "From: $name <$email>";

            #send email.
            $success = mail($mail_to, $subject, $content, $headers);
            if ($success) {
                #response code
                http_response_code(200);
                echo ("<script LANGUAGE='JavaScript'>
                        window.alert('Good news! Your message has been sent.')
                        window.location.href='https://ronnda.info';
                    </script>
                    <NOSCRIPT>
                        <a href='https://ronnda.info'>Good news! Your message has been sent. Click here if you are not redirected.</a>
                    </NOSCRIPT>");
            } else {
                #internal server error response code
                http_response_code(500);
                echo ("<script LANGUAGE='JavaScript'>
                        window.alert('Oops! Something went wrong, your message could not be sent.')
                        window.location.href='https://ronnda.info';
                    </script>
                    <NOSCRIPT>
                        <a href='https://ronnda.info'>Oops! Something went wrong, your message could not be sent. Click here if you are not redirected.</a>
                    </NOSCRIPT>");
            }
        }

    } else {
        #403 (forbidden) response code
        http_response_code(403);
        echo ("<script LANGUAGE='JavaScript'>
                window.alert('There was a problem with your submission, please try again.')
                window.location.href='https://ronnda.info';
            </script>
            <NOSCRIPT>
                <a href='https://ronnda.info'>There was a problem with your submission, please try again. Click here if you are not redirected.</a>
            </NOSCRIPT>");
    }
?>
