<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Creating a Work Item (Issue) using the DevRev API</h1>
    <h3>This is an raw implemmentation for dev rev ... the API could be used in a website or platform to direct to DevRev </h3>
    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>requests</code> library</li>
        <li><code>python-dotenv</code> library</li>
        <li>DevRev API personal access token (PAT)</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository or create a new directory for your project.</li>
        <li>Create a virtual environment (optional but recommended):
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li>Install the required libraries:
            <pre><code>pip install requests python-dotenv</code></pre>
        </li>
        <li>Create a <code>.env</code> file in your project directory and add your DevRev API personal access token:
            <pre><code>PAT=your_personal_access_token</code></pre>
        </li>
      <li>Run Your code to generate issue:
            <pre><code>py main.py</code></pre>
        </li>
    </ol>
</body>
</html>
