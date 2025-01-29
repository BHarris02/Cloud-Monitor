import React, { useEffect, useState } from "react";

const App = () => {
    const [metrics, setMetrics] = useState(null);

    useEffect(() => {
        fetch("/metrics")
        .then(resp => resp.json())
        .then(data => setMetrics(data));
    }, []);

    return (
        <div>
            <h1>Cloud Monitor Dashbaord</h1>
            {metrics && (
                <ul>
                    <li>CPU Usage: {metrics.cpu_usage}%</li>
                    <li>Memory Usage: {metrics.mem_usage}%</li>
                    <li>Disk Usage: {metrics.disk_usage}%</li>
                </ul>
            )}
        </div>
    );
};

export default App;