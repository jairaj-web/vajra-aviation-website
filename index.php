<?php
// Serve static homepage - bypasses WordPress routing
header('Content-Type: text/html; charset=UTF-8');
header('Cache-Control: no-cache, no-store, must-revalidate');
readfile(__DIR__ . '/index.html');
exit;
