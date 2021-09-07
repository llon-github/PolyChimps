# script to call mint.js using Hardhat

import os
import time
import subprocess

startCounter = 2451
endCounter = 2501    # this number has to be the # you want + 1; have no fucking idea why...

# mint while startCounter != endCounter
while startCounter <= endCounter:
    if startCounter >= 1 and startCounter < 10:
        startCounterFormatted = "000" + str(startCounter)
    elif startCounter >= 10 and startCounter < 100:
        startCounterFormatted = "00" + str(startCounter)
    elif startCounter >= 100 and startCounter < 1000:
        startCounterFormatted = "0" + str(startCounter)
    else:
        startCounterFormatted = str(startCounter)

    uri = "const URI = 'https://gateway.pinata.cloud/ipfs/QmcATKyWjwHY9gQa8c9Qbu4aKuZjmvCqxCJrWeKnGTQrTa/{}metadata.json'\n".format(startCounterFormatted)

    f = open("C:\\Users\\Larry\\polygon-nfts\\scripts\\PolyChimps\\mint-script.js", "w")
    f.write(
        "const hre = require('hardhat');\n"
        "async function main() {\n"
            "const NFT = await hre.ethers.getContractFactory('PolyChimps');\n"
            + uri +
            "const WALLET_ADDRESS = '0x35B856346a844957cA3BC365e7279A717550f000'\n"
            "const CONTRACT_ADDRESS = '0x07B64E102dB49bd468A4e5241B643780Cc635F81'\n"
            "const contract = NFT.attach(CONTRACT_ADDRESS);\n"
            "await contract.mint(WALLET_ADDRESS, URI);\n"
            "console.log('NFT minted:', contract);\n"
        "}\n"
        "main().then(() => process.exit(0)).catch(error => {\n"
            "console.error(error);\n"
            "process.exit(1);\n"
        "});\n"
    )

    f.close

    # run the minting script! (25 at a time is the max at once i think)
    os.system("cd C:\\Users\\Larry\\polygon-nfts\\ & npx hardhat run scripts/PolyChimps/mint-script.js --network matic")
    print("NFT #" + str(startCounter) + " Minted")

    startCounter += 1















