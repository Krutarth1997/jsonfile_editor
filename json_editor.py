import json
import streamlit as st


def modify_json(data):
    # Display editable fields
    st.write("Simulation Configuration")
    data["fps"] = st.number_input("Frames per Second", value=data["fps"])
    data["time_step"] = st.number_input("Time Step", value=data["time_step"])
    data["number_agents"] = st.number_input("Number of Agents", value=data["number_agents"])
    data["simulation_time"] = st.number_input("Simulation Time", value=data["simulation_time"])

    ##with data["velocity_model_parameter_profiles"]:
    ##contact_options = ["1", "2"]
    ##contact_selected = st.selectbox("Select agent parameter id", options = contact_options)
    ##if contact_selected == "1":
    ## data["id"] = st.number_input("agent parameter id", value=data["id"])
      ## with data["velocity_model_parameter_profiles"]: 
    for i in data["velocity_model_parameter_profiles"]:
        data["time_gap"] = st.number_input("time_gap", value=data["time_gap"]),
        data["tau"] = st.number_input("tau", value=data["tau"]),
        data["v0"] = st.number_input("v0", value=data["v0"]),
        data["radius"] = st.number_input("radius", value=data["radius"])
        
    return data


def main():
    st.title("JSON Editor")

    # File selection
    json_file = st.file_uploader("Upload JSON File", type=["json"])
    if json_file is not None:
        st.write("File uploaded successfully.")
        data = json.load(json_file)
        modified_data = modify_json(data)

        # Export changes
        if st.button("Export Changes"):
            output_file = "modified_data.json"
            with open(output_file, "w") as file:
                json.dump(modified_data, file, indent=4)
            st.success(f"Changes exported to {output_file}")


if __name__ == "__main__":
    main()
