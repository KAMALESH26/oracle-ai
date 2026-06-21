import {
  FaChartLine,
  FaRobot,
  FaBrain,
  FaHome,
  FaFileAlt
} from "react-icons/fa";

function Sidebar() {

  return (

    <div className="sidebar">

      <h2>ORACLE AI</h2>

      <ul>

        <li>
          <FaHome />
          Overview
        </li>

        <li>
          <FaChartLine />
          Trends
        </li>

        <li>
          <FaBrain />
          Forecasts
        </li>

        <li>
          <FaFileAlt />
          Reports
        </li>

        <li>
          <FaRobot />
          Agent
        </li>

      </ul>

    </div>
  );
}

export default Sidebar;