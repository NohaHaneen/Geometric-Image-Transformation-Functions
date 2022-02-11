import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import CircularProgress from '@mui/material/CircularProgress';

export default function MediaCard() {
	return (
		<Card sx={{ maxWidth: 445 }}>
			<CardContent>
				<div style={{ height: 340, width: 445, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
					No Image
				</div>
			</CardContent>
		</Card>
	);
}

export function InputNoImageCard() {
	return (
		<Card sx={{ maxWidth: 445 }}>
			<CardContent>
				<div style={{ height: 340, width: 445, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
					No Image
				</div>
			</CardContent>
		</Card>
	);
}

const onClickImage = (e) => {
	console.log(e.nativeEvent.offsetY)
	console.log(e.nativeEvent.offsetX)
}

export function InputImageCard(props) {
	return (
		<Card sx={{ maxWidth: 445 }}>
			<CardMedia
				component="img"
				height="340"
				image={`data:image/*;base64,${props.imageURL}`}
				alt="input image"
				onClick={onClickImage}
			/>
		</Card>
	);
}

export function OutputNoImageCard(props) {
	return (
		<Card sx={{ maxWidth: 445 }}>
			<CardContent>
				<div style={{ height: 340, width: 445, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

					{props.isLoading && 
						<><CircularProgress /></>
					}
					{!props.isLoading && 
						'No Image'
					}
				</div>
			</CardContent>
		</Card>
	);
}

export function OutputImageCard(props) {
	return (
		<Card sx={{ maxWidth: 445 }}>
			<CardMedia
				component="img"
				height="340"
				image={`data:image/*;base64,${props.imageURL}`}
				alt="output image"
			/>
		</Card>
	);
}
