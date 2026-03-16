import json

def generate_html_report(results, vuln_count, total_tests):

    html = f"""
    <html>
    <head>
        <title>Smart Fuzzer Report</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                padding: 20px;
            }}

            h1 {{
                color: #333;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
            }}

            th, td {{
                padding: 10px;
                border: 1px solid #ccc;
            }}

            th {{
                background: #333;
                color: white;
            }}

            .safe {{
                color: green;
                font-weight: bold;
            }}

            .suspicious {{
                color: red;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

    <h1>Smart AI Fuzzer Security Report</h1>

    <p><b>Total Tests:</b> {total_tests}</p>
    <p><b>Vulnerabilities Detected:</b> {vuln_count}</p>

    <table>
    <tr>
        <th>Prompt</th>
        <th>Status</th>
    </tr>
    """

    for item in results:

        status_class = "safe"

        if item["status"] == "SUSPICIOUS":
            status_class = "suspicious"

        html += f"""
        <tr>
            <td>{item['prompt']}</td>
            <td class="{status_class}">{item['status']}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\nHTML Report Generated: report.html")