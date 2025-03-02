# 🎉 Event Planner AI Agent (CrewAI + UV Package Manager)

Welcome to the **Event Planner AI Agent**! This AI-powered system leverages the **CrewAI framework** to automate event planning tasks, from **venue selection and logistics management** to **event marketing**. Built using **UV Package Manager**, it ensures efficient dependency management and seamless execution.

---

## 🚀 Key Features  

- 🔹 **Venue Selection:** Finds and secures the perfect venue based on event requirements.  
- 🔹 **Logistics Management:** Handles catering, equipment setup, and other event logistics.  
- 🔹 **Marketing & Engagement:** Promotes the event and engages with potential attendees.  
- 🔹 **Agentic Workflow:** Uses **CrewAI agents** to autonomously complete tasks.  
- 🔹 **Scalability:** Easily adaptable for different event types and sizes.  

---

## 🧑‍💼 AI Agents & Responsibilities
This system is powered by three intelligent CrewAI agents, each with a unique role:

🏛 1. Venue Coordinator Agent
📌 Goal: Identify and book a suitable venue.
📌 Role: Finds venues that match event size, theme, and budget.
📌 Backstory: Skilled in event logistics, ensuring the best location for an event.

# Assigned Task:

venue_task:
  description: >
    Find a venue in {event_city} 
    that meets criteria for {event_topic}
  expected_output: >
    All the details of a specifically chosen
    venue you found to accommodate the event
  agent: Venue_Coordinator_Agent
🚛 2. Logistics Manager Agent
📌 Goal: Manage catering, equipment, and event logistics.
📌 Role: Ensures all logistical aspects are seamlessly handled.
📌 Backstory: Detail-oriented and efficient in executing catering, setup, and equipment management.

# Assigned Task:
logistics_task: 
  description: >
    Coordinate catering and 
    equipment for an event 
    with {expected_participants} participants 
    on {tentative_date}
  expected_output: >
    Confirmation of all logistics arrangements
    including catering and equipment setup
  agent: logistics_manager_Agent
📢 3. Marketing & Communications Agent
📌 Goal: Promote the event and engage participants.
📌 Role: Creates marketing campaigns and communicates with attendees.
📌 Backstory: A creative strategist who maximizes event visibility and participation.

# Assigned Task:

marketing_task: 
  description: >
    Promote the {event_topic}
    aiming to engage at least
    {expected_participants} potential attendees
  expected_output: >
    Report on marketing activities
    and attendee engagement formatted as markdown
  agent: marketing_communications_Agent

  
## 🛠️ Installation & Setup
🔧 1. Install UV Package Manager & Dependencies
Ensure you have UV (UltraFast Python Package Manager) installed:

pip install uv
Then, install required dependencies:

uv pip install crewai pandas streamlit
🚀 2. Running the Event Planner AI
Run the CrewAI event planner script:

python event_planner.py
This initializes the agentic workflow, and each agent autonomously executes its task.

## 📌 Folder Structure

📂 Event-Planner-AI
│── 📂 agents
│   ├── venue_coordinator.py
│   ├── logistics_manager.py
│   ├── marketing_agent.py
│── 📂 tasks
│   ├── venue_task.yaml
│   ├── logistics_task.yaml
│   ├── marketing_task.yaml
│── 📜 event_planner.py
│── 📜 README.md



## 📊 Example Workflow
📍 User Input:

Event Topic: Tech Conference
Expected Participants: 500
Event Date: June 20, 2025
Event City: New York
📍 Output:

✅ Venue Coordinator Agent: Finds and books a venue in New York that accommodates 500 attendees.
✅ Logistics Manager Agent: Confirms catering and AV equipment for the event.
✅ Marketing Agent: Generates a marketing campaign report with attendee engagement details.

## 🌟 Future Enhancements
🔹 AI-powered Venue Recommendations using location-based APIs.
🔹 Automated Budget Management to optimize costs.
🔹 Real-time Analytics Dashboard for event insights.
🔹 Multi-Agent Collaboration with additional roles (Security, Guest Management, etc.).
💡 Conclusion
This AI-powered Event Planner automates and streamlines event organization using CrewAI agents. From venue selection to logistics and marketing, it provides a smart and scalable event planning solution. 🎉

🚀 Get Started Today and Plan Your Event with AI!

