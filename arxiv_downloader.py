import os
import sys
import tarfile
import urllib.request
import argparse

def download_arxiv_source(arxiv_id, output_dir):
    """Downloads the source files for an arXiv paper and extracts them."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    url = f"https://arxiv.org/e-print/{arxiv_id}"
    tarball_path = os.path.join(output_dir, f"{arxiv_id}.tar.gz")

    print(f"Downloading source for arXiv:{arxiv_id} from {url}...")
    try:
        urllib.request.urlretrieve(url, tarball_path)
    except Exception as e:
        print(f"Error downloading from {url}: {e}")
        return False

    print(f"Extracting to {output_dir}...")
    try:
        with tarfile.open(tarball_path, "r:gz") as tar:
            tar.extractall(path=output_dir)
        print("Extraction complete.")
    except Exception as e:
        print(f"Error extracting {tarball_path}: {e}")
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and extract arXiv source files.")
    parser.add_argument("arxiv_id", help="The arXiv ID (e.g., 0902.1089 or 1502.02866)")
    parser.add_argument("--output", "-o", default=".", help="Output directory (default: current directory)")
    
    args = parser.parse_args()
    
    output_path = os.path.join(args.output, args.arxiv_id.replace("/", "_"))
    download_arxiv_source(args.arxiv_id, output_path)
