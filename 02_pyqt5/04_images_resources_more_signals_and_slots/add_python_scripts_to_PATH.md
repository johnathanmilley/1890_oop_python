Add Python Scripts folder to System Path

1. Run `pip --version` in PowerShell or Command Prompt
2. Copy the file path up to Python39 (the version) and add the Scripts folder
    Here's mine: 
    
    C:\Users\john.milley\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts

3. Hit the **Windows key** and search for "Environment Variables" or "Advanced System Settings". Either should get you to a System Properties window.

4. Click the **Environment Variables…** button on the bottom-right of the Advanced tab.

5. Highlight the Path variable under "User variables for [username]" and click the **Edit…** button.

1. Click **New** and paste in the path copied in Step 2.

2. Click **OK**, and close the remaining windows.
