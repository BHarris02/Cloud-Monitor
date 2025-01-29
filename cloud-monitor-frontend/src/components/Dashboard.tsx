import React from "react";
import MetricsCard from "./MetricsCard";

const Dashboard = ({ metrics }) => {
    return (
        <div>
            <h1>Cloud Monitoring Dashboard</h1>
            <MetricsCard label={"CPU Usage"} value={metrics.cpu_usage} unit={"%"} />
            <MetricsCard label={"Memory Usage"} value={metrics.mem_usage} unit={"%"} />
            <MetricsCard label={"Disk Usage"} value={{metrics.disk_usage}} unit={"%"} />
        </div>
    );
};