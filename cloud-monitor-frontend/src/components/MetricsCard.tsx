import React from "react";

const MetricsCard = ({ label, value, unit }) => {
    return (
        <div>
            <h3>{label}</h3>
            <p>{value}{unit}</p>
        </div>
    );
};

export default MetricsCard;