export const fetchMetrics = async () => {
    const resp = await fetch("/metrics");
    return resp.json();
}