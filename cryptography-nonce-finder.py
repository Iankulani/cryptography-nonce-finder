import hashlib
import sys

def find_nonce_with_leading_zeros(data_prefix="", required_zeros=5):
    """
    Find a nonce such that SHA256(data_prefix + str(nonce)) starts with required_zeros zeros.
    
    Args:
        data_prefix (str): The base data to hash
        required_zeros (int): Number of leading zeros required
        
    Returns:
        tuple: (nonce, hash_value) where hash_value starts with required_zeros zeros
    """
    # Create the target prefix (e.g., "00000" for 5 zeros)
    target_prefix = "0" * required_zeros
    
    # Start with nonce = 0 and increment
    nonce = 0
    
    while True:
        # Combine the data prefix with the nonce
        input_data = data_prefix + str(nonce)
        
        # Calculate SHA256 hash
        hash_result = hashlib.sha256(input_data.encode()).hexdigest()
        
        # Check if hash starts with the required number of zeros
        if hash_result.startswith(target_prefix):
            return nonce, hash_result
            
        # Increment nonce for next iteration
        nonce += 1
        
        # Optional: Add a progress indicator for very long searches
        if nonce % 1000000 == 0:
            print(f"Tried {nonce:,} nonces...", file=sys.stderr)

def main():
    """Main function to demonstrate the nonce finding process."""
    # You can customize the data prefix if needed
    data_prefix = "Hello, World! "
    
    print("Searching for a nonce that produces a SHA256 hash starting with 5 zeros...")
    print(f"Data prefix: '{data_prefix}'")
    print("This might take a moment...\n")
    
    try:
        # Find the nonce
        nonce, hash_value = find_nonce_with_leading_zeros(data_prefix, required_zeros=5)
        
        # Print the results
        print(f"Found nonce: {nonce}")
        print(f"Input data: '{data_prefix + str(nonce)}'")
        print(f"SHA256 hash: {hash_value}")
        print(f"✓ Hash starts with '00000': {hash_value.startswith('00000')}")
        
        return nonce, hash_value
        
    except KeyboardInterrupt:
        print("\n\nSearch interrupted by user.")
        sys.exit(1)

if __name__ == "__main__":
    nonce, hash_value = main()