import { useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "https://ai-agent-api-hp1r.onrender.com/api";

function App() {
  const [activeTab, setActiveTab] = useState("workflow");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [response, setResponse] = useState(null);

  const [workflowTask, setWorkflowTask] = useState("");
  const [singleAgentType, setSingleAgentType] = useState("planner");
  const [singleAgentMessage, setSingleAgentMessage] = useState("");
  const [toolAgentMessage, setToolAgentMessage] = useState("");

  const handleWorkflow = async () => {
    setLoading(true);
    setError("");
    setResponse(null);
    try {
      const res = await axios.post(`${API_URL}/workflow`, {
        task: workflowTask,
      });
      setResponse(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong");
    }
    setLoading(false);
  };

  const handleSingleAgent = async () => {
    setLoading(true);
    setError("");
    setResponse(null);
    try {
      const res = await axios.post(`${API_URL}/agent`, {
        agent: singleAgentType,
        message: singleAgentMessage,
      });
      setResponse(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong");
    }
    setLoading(false);
  };

  const handleToolAgent = async () => {
    setLoading(true);
    setError("");
    setResponse(null);
    try {
      const res = await axios.post(`${API_URL}/tool-agent`, {
        message: toolAgentMessage,
      });
      setResponse(res.data);
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong");
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <header className="header">
        <h1>AI Agent System</h1>
        <p>Multi-agent orchestration with tools and guardrails</p>
      </header>

      <div className="tabs">
        <button
          className={`tab-button ${activeTab === "workflow" ? "active" : ""}`}
          onClick={() => setActiveTab("workflow")}
        >
          Workflow
        </button>
        <button
          className={`tab-button ${activeTab === "single" ? "active" : ""}`}
          onClick={() => setActiveTab("single")}
        >
          Single Agent
        </button>
        <button
          className={`tab-button ${activeTab === "tool" ? "active" : ""}`}
          onClick={() => setActiveTab("tool")}
        >
          Tool Agent
        </button>
      </div>

      <div className="panel">
        {activeTab === "workflow" && (
          <div>
            <div className="input-group">
              <label>Task Description</label>
              <textarea
                value={workflowTask}
                onChange={(e) => setWorkflowTask(e.target.value)}
                placeholder="Example: Write a blog post about artificial intelligence"
              />
            </div>
            <button
              className="submit-button"
              onClick={handleWorkflow}
              disabled={loading || !workflowTask}
            >
              {loading ? "Processing..." : "Run Workflow"}
            </button>
          </div>
        )}

        {activeTab === "single" && (
          <div>
            <div className="input-group">
              <label>Select Agent</label>
              <select
                value={singleAgentType}
                onChange={(e) => setSingleAgentType(e.target.value)}
              >
                <option value="planner">Planner</option>
                <option value="researcher">Researcher</option>
                <option value="writer">Writer</option>
              </select>
            </div>
            <div className="input-group">
              <label>Message</label>
              <textarea
                value={singleAgentMessage}
                onChange={(e) => setSingleAgentMessage(e.target.value)}
                placeholder="Enter your message for the agent"
              />
            </div>
            <button
              className="submit-button"
              onClick={handleSingleAgent}
              disabled={loading || !singleAgentMessage}
            >
              {loading ? "Processing..." : "Run Agent"}
            </button>
          </div>
        )}

        {activeTab === "tool" && (
          <div>
            <div className="input-group">
              <label>Message</label>
              <textarea
                value={toolAgentMessage}
                onChange={(e) => setToolAgentMessage(e.target.value)}
                placeholder="Example: Search for information about Python"
              />
            </div>
            <button
              className="submit-button"
              onClick={handleToolAgent}
              disabled={loading || !toolAgentMessage}
            >
              {loading ? "Processing..." : "Run Tool Agent"}
            </button>
          </div>
        )}

        {loading && <div className="loading">Processing your request...</div>}

        {error && <div className="error">{error}</div>}

        {response && (
          <div className="response-box">
            <h3>Response</h3>
            {activeTab === "workflow" && response.workflow_log && (
              <div>
                {response.workflow_log.map((step, index) => (
                  <div key={index} className="workflow-step">
                    <h4>{step.agent}</h4>
                    <p>{step.output}</p>
                  </div>
                ))}
              </div>
            )}
            {activeTab === "single" && (
              <div>
                <p>
                  <strong>Agent:</strong> {response.agent}
                </p>
                <p>{response.response}</p>
              </div>
            )}
            {activeTab === "tool" && (
              <div>
                <p>{response.response}</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
