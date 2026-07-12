Read the Apache access log located at /app/access.log and generate a JSON summary report.

Write the output to:

/app/report.json

Success criteria:

1. Create /app/report.json.
2. The file must contain valid JSON.
3. Include total_requests containing the total number of log entries.
4. Include unique_ips containing the number of unique client IP addresses.
5. Include top_path containing the most frequently requested path.
