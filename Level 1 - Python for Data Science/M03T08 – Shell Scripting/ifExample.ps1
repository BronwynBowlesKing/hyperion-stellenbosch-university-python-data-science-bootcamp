# Show the current working directory
Write-Host "Current directory: $(Get-Location)"

# Set the working directory to Downloads
Set-Location "C:\Users\36050\Downloads"

# Confirm the change to Downloads
Write-Host "Now in directory: $(Get-Location)"

# Create a new sub-folder (if_folder) if a specific folder (new_folder) exists and inside it. If new_folder does not exist, if_folder will not be created
if (Test-Path "new_folder") {
    New-Item -ItemType Directory -Path "new_folder\if_folder"
    Write-Host "'if_folder' was created inside 'new_folder'."
} else {
    Write-Host "'new_folder' does not exist. 'if_folder' was not created."
}

# Create a new sub-folder (hyperionDev) if a specific folder (if_folder) exists and inside it. If if_folder does not exist, hyperionDev folder will be created instead
if (Test-Path "if_folder") {
    New-Item -ItemType Directory -Path "if_folder\hyperionDev"
    Write-Host "'hyperionDev' was created inside 'if_folder'."
} else {
    New-Item -ItemType Directory -Path "new_projects"
    Write-Host "'if_folder' does not exist. 'new_projects' was created instead."
}
