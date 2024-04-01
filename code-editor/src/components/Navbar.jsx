import React, { useState } from 'react';

function Navbar() {
    const [isDarkMode, setIsDarkMode] = useState(false);

    const handleNewFile = () => {
        window.location.reload(); // Reloads the page
    };

    const handleFullscreen = () => {
        if (document.fullscreenEnabled) {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
            } else {
                document.exitFullscreen();
            }
        }
    };

    const toggleTheme = () => {
        setIsDarkMode(!isDarkMode);
        document.body.classList.toggle('dark-mode'); 
    };

    return (
        <nav className="bg-black p-4">
            <div className="flex items-center justify-between">
                <div className="flex items-center">
                    <img src="/IMG/pic.jpeg" className="max-w-xl rounded-lg w-64 h-20" alt="Description of image" />
                    <div className="p-4">
                        <h1 className="text-2xl font-bold mb-4 text-gray-50 pl-30">Welcome to Code Editor</h1>
                    </div>
                </div>
                <div className="flex justify-end p-4">
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2 cursor-pointer" onClick={handleNewFile}>New File</button>
                    <button className="bg-green-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-2" onClick={handleFullscreen}>Fullscreen</button>

                </div>
            </div>
        </nav>
    );
}

export default Navbar;
