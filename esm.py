import os
import json

print("Current Directory", os.getcwd())

readTsConfig = open(os.getcwd() + r"\tsconfig.json").read().splitlines()

#remove json comments. TODO: parse so that comments are kept when dumped
tsConfig = json.loads("\n".join(line for line in readTsConfig if "//" not in line and "/*" not in line))
tsConfig["compilerOptions"]["target"] = "es2020"
tsConfig["compilerOptions"]["lib"] = ["es2020"]
tsConfig["compilerOptions"]["module"] = "ESNext"
tsConfig["compilerOptions"]["moduleResolution"] = "node16"
tsConfig["compilerOptions"]["isolatedModules"] = True
tsConfig["compilerOptions"]["noPropertyAccessFromIndexSignature"] = True

tsConfig["ts-node"] = {
    "transpileOnly": True,
    "files": True,
    "esm": True,
    "experimentalResolver": True
}

with open('tsconfig.json','w') as f:
    json.dump(tsConfig, f, indent=2)

package = json.load(open(os.getcwd() + r"\package.json"))
package["type"] = "module"
del package["main"]
package["exports"] = "./index.js"
package["engines"] = {
    "node": ">=14.16"
}
with open('package.json','w') as f:
    json.dump(package, f, indent=4)

print("Done.")
