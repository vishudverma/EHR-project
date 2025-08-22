import pkg_resources
import subprocess
import sys
from pathlib import Path

def check_requirements():
    """Check if all packages in requirements.txt are installed with correct versions."""
    requirements_path = Path(__file__).parent.parent.parent / 'requirements.txt'
    
    if not requirements_path.exists():
        print("Warning: requirements.txt not found!")
        return
    
    # Read requirements from file
    with open(requirements_path) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # Check each requirement
    missing = []
    outdated = []
    
    for requirement in requirements:
        try:
            pkg_resources.require(requirement)
        except pkg_resources.DistributionNotFound:
            missing.append(requirement)
        except pkg_resources.VersionConflict as e:
            outdated.append((requirement, e.dist.version))
    
    if missing or outdated:
        print("\n⚠️ Environment Check Results:")
        print("-" * 50)
        
        if missing:
            print("\nMissing packages:")
            for pkg in missing:
                print(f"  • {pkg}")
        
        if outdated:
            print("\nOutdated packages:")
            for pkg, version in outdated:
                print(f"  • {pkg} (current: {version})")
        
        print("\nWould you like to install/update these packages? [y/N]")
        response = input().lower()
        
        if response == 'y':
            print("\nUpdating packages...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_path)])
            print("\n✅ Packages updated successfully!")
    else:
        print("\n✅ All requirements are satisfied!")

if __name__ == "__main__":
    check_requirements()
