# Show the current working directory
Write-Host "Current directory: $(Get-Location)"

# Set the working directory to Documents
Set-Location "C:\Users\36050\OneDrive\Documents"

# Confirm the change to Documents
Write-Host "Now in directory: $(Get-Location)"

# Create the three folders in the current directory
New-Item -ItemType Directory -Path "Dinosaurs"
New-Item -ItemType Directory -Path "Team_List"
New-Item -ItemType Directory -Path "Flowers"

# Navigate to a specific folder
Set-Location ".\Dinosaurs"

# Create the three sub-folders 
New-Item -ItemType Directory -Path "Deinonychus"
New-Item -ItemType Directory -Path "Iguanodon"
New-Item -ItemType Directory -Path "Aardonyx"

# Permanently delete a folder in "Dinosaurs"
Remove-Item -Path "Deinonychus" -Recurse -Force

# Return to the parent folder "Documents"
Set-Location ..

# Or for this purpose, you can also use:
# Set-Location "C:\Users\36050\OneDrive\Documents"

# Permanently delete a folder in "Documents"
Remove-Item -Path "Team_List" -Recurse -Force