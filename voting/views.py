from django.shortcuts import render
from web3 import Web3
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ✅ Step 1: Connect to the local blockchain (Ganache)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Check if the connection is successful
if not web3.is_connected():
    raise Exception("Failed to connect to blockchain")

# ✅ Step 2: Load contract ABI & Address
try:
    with open("build/contracts/Voting.json") as f:  # Ensure path is correct
        contract_json = json.load(f)
        contract_abi = contract_json["abi"]
except FileNotFoundError:
    raise Exception("Contract ABI file not found. Check the path.")

# Replace with your actual deployed contract address
contract_address = "0x865E780b086960D4B8CEb3961fd7cf411E4fE5ae"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# ✅ Step 3: Define API Endpoints

@csrf_exempt  # Remove this in production
def cast_vote(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            candidate = data.get("candidate")

            if not candidate:
                return JsonResponse({"error": "Candidate is required"}, status=400)

            # Get a test Ethereum account from Ganache
            voter_accounts = web3.eth.accounts[0]  # Fetch accounts dynamically
            if not voter_accounts:
                return JsonResponse({"error": "No Ethereum accounts available"}, status=500)

            voter_address = web3.eth.accounts[0]  # ✅ Correct
# Select first test account

            # Call smart contract vote function
            tx_hash = contract.functions.vote(candidate).transact({"from": voter_address})
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

            return JsonResponse({"message": "Vote cast successfully!", "tx_hash": receipt.transactionHash.hex()})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def get_votes(request):
    if request.method == "GET":
        try:
            candidate = request.GET.get("candidate")

            if not candidate:
                return JsonResponse({"error": "Candidate is required"}, status=400)

            # Call smart contract function to get vote count
            vote_count = contract.functions.getVotes(candidate).call()

            return JsonResponse({"candidate": candidate, "votes": vote_count})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
