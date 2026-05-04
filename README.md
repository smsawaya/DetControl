Detonation Controls Code for ARL at UVA

REPOSITORY AND CODE ARCHITECTURE: 

- All code for the full facility is located under Full Scale Facility folder. Old codes (for initiator testing and general GUI testing) are located under Initiator and Old Test Code. 

- .gitignore tells Git what files not to track (i.e. personal virtual environments and caches) 

- requirements.txt includes all required libraries. if opening repo on new computer, run "pip install -r requirements.txt" 

File that Runs the Control GUI: full_facility_gui.py 
- this is the code that actually starts up the GUI and maps all GUI buttons/features to actions 
- contains the following "workers" that are able to thread actions simultaneously
        -MFCMonitorWorker that continually updates the MFC flow indicators on the GUI 
        -AutomationWorker that runs the test without driver as well as the purge functions
        -DriverWorker that runs the tests with driver 
        -SolenoidWorker that is used to toggle solenoids and run the ignite button 
- runs the following functions: 
        - maps ignite, vacuum down, purge, test buttons to their corresponding functions
        - auto updates pressure based on if auto read buttons are on/off 
        - bnc arming and mode buttons 
        - maps solenoid control buttons to NI states 
        - updates solenoid state labels based on NI states 


Main Facility Testing File: full_facility_run_methods.py 
- this is the code that actually runs the tests both with and without drivers as well as the purge function 
- as tests run, this code sets flow rates, solenoid states, and calls csv logging functions 

GUI Design Scripts: ui_full_facility_script.ui and .py 
- these can be edited easily using Qt Widgets Designer 
- when editing in the designer, make sure to also save as .py, as full_facility_gui calls this .py file when starting up the GUI 
- each GUI object has a name that is referenced in the code. names can be edited using the object editor in QT Widgets Designer 




Helper Functions: 

- nicontrol.py 
    - this is the code that interfaces with the NI DAQs 
    - set_digital_output and set_digital_output2 control the 2 digital output DAQs, sending ON/OFF states to solenoids and other electronics 
    - set_mfc_setpoints_analog sends analog signals to the MFCs to control flow rates 
    - acquire_mfc_fill_log reads the MFCs actual flow rates and the pressure during the fill phase 
    - laser_ignite_read_pressure and spark_ignite_read_pressure are the two ignition functions that send ignite signals and trigger the pressure taps to read as the wave propagates down the tunnel. which one runs is dependent on which ignition mode the code is in 
    -read_vacuum_pressure and read_pressure used to read the pressure gauge readings and convert to kPa or Pa 

- bnc_box_control.py
    -this code is used to interface with the BNC control boxes
    - contains two functions: 
        - arm sends :PULSE0:STATE:ON or OFF to the box, acting as the RUN/STOP button
        - switch_preset tells the boxes which preset to switch two 
        - both functions contain an argument to tell the code which COM port to connect to (which box to interface with)

- klinger_control.py
    -same idea as bnc_box_control.py but for the Klinger stepping motor 
    -serial control functions used to move the motor back and forth 

- audio_player.py 
    -uses pyttsx3 library for text to speech functions 

- alicatcontrol.py 
    - was originally used for all commands to the Alicats using serial communication
    - now used for two main serial-based functions: 
        - change_gas uses serial commands to change the gases of each MFC 
        - MFCMonitorWorker continually polls read_flows() every second to display flow values to the GUI even during fills where the analog voltage is read by the NI DAQs 

- fill_log_csv.py 
    - takes raw data from fill_log_csv.py in nicontrol and converts it to a labeled CSV file 
    - segments() functions build a table with phase names and event labels 
    - fill_log_rows_from_acquisition walks through every sample from the fill data and assigns it to a segment 
    - write_fill_flow_rates then takes the labeled rows and writes them to a csv file 


