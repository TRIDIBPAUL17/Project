import React from 'react';

function Features({ icon, name }) {
    return (
        <div className="flex items-center mr-4 cursor-pointer">
            <div className="mr-2">{icon}</div>
            <div>{name}</div>
        </div>
    );
}

export default Features;
