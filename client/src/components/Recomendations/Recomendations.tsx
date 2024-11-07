import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Marquee from "@/components/ui/marquee";

const backendUrl = import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000';

const Recomendations: React.FC = () => {
    const [suggestions, setSuggestions] = useState<string[]>([]);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const fetchSuggestions = async () => {
            const username = localStorage.getItem('devhub_username');

            if (!username) {
                setError('Username not found in local storage');
                setLoading(false);
                return;
            }

            try {
                const response = await axios.get(`${backendUrl}/suggestions/${username}`);
                setSuggestions(response.data.suggestions);
            } catch (err) {
                setError('Error fetching suggestions');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        fetchSuggestions();
    }, []);

    return (
        <div>
            {loading && <p>Loading...</p>}
            {error && <p>{error}</p>}
            {suggestions.length > 0 && (
                <ul className='flex items-center justify-center'>
                    <Marquee pauseOnHover vertical className="[--duration:20s]">
                            {suggestions.map((suggestion, index) => (
                                <div className="flex items-center border border-gray-300 rounded-lg">
                                    <div className="p-4 flex items-center space-x-4">
                                        <div className="h-6 w-6 rounded-full bg-gradient-to-r from-pink-500 to-violet-500 flex-shrink-0" />
                                        <a href={`/user/${suggestion}`}>
                                            <li key={index} className="list-none">@{suggestion}</li>
                                        </a>
                                        
                                    </div>
                                </div>
                            ))}
                    </Marquee>
                    
                </ul>
            )}
            {suggestions.length === 0 && !loading && <p>No suggestions available.</p>}
        </div>
    );
};

export default Recomendations;
