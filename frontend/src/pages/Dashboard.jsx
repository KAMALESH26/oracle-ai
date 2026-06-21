import MainLayout from "../layout/MainLayout";

import Navbar from "../components/Navbar";
import StatsCards from "../components/StatsCards";
import TrendTable from "../components/TrendTable";
import ReportCard from "../components/ReportCard";
import OracleChat from "../components/OracleChat";
import TrendCards from "../components/TrendCards";
import TrendGrowthChart from "../charts/TrendGrowthChart";
import InsightsPanel from "../components/InsightsPanel";
import MomentumCards from "../components/MomentumCards";
import ForecastCards from "../components/ForecastCards";
import TopicForecastCards
from "../components/TopicForecastCards";
import TopicHistoryChart
from "../charts/TopicHistoryChart";


function Dashboard() {

  return (

    <div className="dashboard-container">

        <MainLayout>

        <Navbar />

        <StatsCards />

        <TrendGrowthChart />

        <TopicHistoryChart />

        <TrendCards />

        <MomentumCards />

        <ForecastCards />

        <InsightsPanel />

        <TopicForecastCards />

        {/* <ReportCard /> */}

        <OracleChat />

        </MainLayout>

    </div>

  );
}

export default Dashboard;
