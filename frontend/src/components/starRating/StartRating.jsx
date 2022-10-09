import React from 'react'
import StarIcon from '@mui/icons-material/Star';
import StarHalfIcon from '@mui/icons-material/StarHalf';

const StartRating = ({ count, size }) => {
    const startArr = [];
    for (let i = 0; i < Math.trunc(count); i++) {
        startArr.push(1);
    }
    if (Math.trunc(count) !== count) {
        startArr.push(0.5)
    }

    return (
        <div>
            {
                startArr.map((val, idx) => val === 1
                    ? <StarIcon key={idx} size={size} color='warning' />
                    : <StarHalfIcon key={idx} size={size} color='warning' />)
            }
        </div>
    )
}

export default StartRating