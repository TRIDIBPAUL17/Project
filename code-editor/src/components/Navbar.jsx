import React from 'react';

function Navbar() {
    const handleNewFile = () => {
        window.location.reload(); // Reloads
    };

    return (
        <nav className="bg-black p-4">
            <div className="flex items-center justify-between">
                <div className="flex items-center">
                <img src="src/components/pic.jpeg" class=" max-w-xl rounded-lg w-64 h-20" alt="Description of image"></img>
                <div className="p-4">
                <h1 className="text-2xl font-bold mb-4 text-gray-50 pl-30">Welcome to Code Editor</h1>
            </div>
                </div>
                <div class="flex justify-end p-4">
                    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2 cursor-pointer "onClick={handleNewFile}>New File</button>
                    <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2">Log in</button>
                    <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">Sign Up</button>
                </div>

            </div>
        </nav>
    );
}

export default Navbar;
