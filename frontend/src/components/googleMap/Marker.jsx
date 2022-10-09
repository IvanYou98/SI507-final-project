import React from 'react'
import LocationOnIcon from '@mui/icons-material/LocationOn';
import Tooltip from '@mui/material/Tooltip';

const Marker = ({ $hover, tooltip }) => {
    return (
        <div>
            <Tooltip title={tooltip}>
                <LocationOnIcon color='error' />
            </Tooltip>
        </div>
    )
}

export default Marker