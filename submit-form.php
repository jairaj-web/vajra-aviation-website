<?php
/**
 * Vajra Aviation — Contact Form Handler
 * Sends form submissions to vajraaviationlimited@gmail.com
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://vajraaviation.com');
header('Access-Control-Allow-Methods: POST');

// Only accept POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// Sanitize inputs
function clean($val) {
    return htmlspecialchars(strip_tags(trim($val)), ENT_QUOTES, 'UTF-8');
}

$name    = clean($_POST['name']    ?? '');
$phone   = clean($_POST['phone']   ?? '');
$email   = clean($_POST['email']   ?? '');
$course  = clean($_POST['course']  ?? '');
$education = clean($_POST['education'] ?? '');
$city    = clean($_POST['city']    ?? '');
$message = clean($_POST['message'] ?? '');
$source  = clean($_POST['source']  ?? 'Website');

// Basic validation
if (empty($name) || empty($phone)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Name and phone are required']);
    exit;
}

// Validate email if provided
if (!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid email address']);
    exit;
}

// Build email
$to      = 'vajraaviationlimited@gmail.com';
$subject = "New Enquiry: {$name} — {$course}";

$body = "
NEW ENQUIRY FROM VAJRA AVIATION WEBSITE
========================================

Name:        {$name}
Phone:       {$phone}
Email:       {$email}
Course:      {$course}
Education:   {$education}
City:        {$city}
Source:      {$source}

Message:
{$message}

========================================
Submitted: " . date('d M Y, h:i A') . "
IP: " . $_SERVER['REMOTE_ADDR'] . "
";

$headers  = "From: noreply@vajraaviation.com\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$sent = mail($to, $subject, $body, $headers);

if ($sent) {
    echo json_encode(['success' => true, 'message' => 'Message sent successfully']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Failed to send. Please call us directly.']);
}
?>
