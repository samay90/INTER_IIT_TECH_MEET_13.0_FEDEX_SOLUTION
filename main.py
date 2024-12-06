from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from utils.package import Package
from utils.uld import ULD
from distribution.divider import divider
app = Flask(__name__)
cors = CORS(app)  # allow CORS for all domains on all routes.
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/get-coords", methods=["POST"])
@cross_origin()
def get_coords():
    priority_uld_cost = request.json["priority_uld_cost"]
    packages = request.json["packages"]
    ulds = request.json["ulds"]
    package_list = []
    for package in packages:
        pkg = Package(
            package["name"],
            package["length"],
            package["width"],
            package["height"],
            package["weight"],
            package["isPriority"],
            package["delayCost"],
        )
        package_list.append(pkg)

    uld_list = []
    for uld in ulds:

        uld_list.append(
            ULD(
                name=uld["name"],
                length=uld["length"],
                width=uld["width"],
                height=uld["height"],
                max_weight=uld["maxWeight"],
            )
        )
    data = divider(uld_list,package_list)
    return {
        "data":data,
        "length":len(data)
    }




if __name__ == "__main__":
    app.run(debug=True, port=5000)
