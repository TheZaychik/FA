import * as React from 'react';
import {Text, View, StyleSheet} from 'react-native';
import Constants from 'expo-constants';

// You can import from local files
import AssetExample from './components/AssetExample';

// or any pure javascript modules available in npm
import {Card} from 'react-native-paper';

export default function App() {
    return (
        <View style={styles.container}>
            <Text style={styles.paragraph}>
                Vitae viverra ante finibus et
            </Text>
            <Card>
                <Text style={styles.center}>
                    In aliquam dapibus ex, vitae viverra ante finibus et
                </Text>
                <Card style={{backgroundColor: '#808080'}}>
                    <Text style={{margin: 10}}>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sit amet vehicula ante. Proin
                        sapien urna, aliquam eget scelerisque quis, tempus et est. Curabitur eleifend dapibus volutpat.
                        Etiam elementum, est non faucibus congue, est nunc mollis ante, in rutrum magna enim et quam.
                        Mauris malesuada euismod aliquet. Vestibulum blandit dapibus lorem id lobortis. Aliquam erat
                        volutpat. Fusce dignissim eleifend ligula quis semper. Nullam luctus eu lacus nec malesuada. In
                        aliquam dapibus ex, vitae viverra ante finibus et. Aenean tellus lacus, varius vel scelerisque
                        sed, euismod eu ex.
                    </Text>
                </Card>
            </Card>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        paddingTop: Constants.statusBarHeight,
        backgroundColor: '#ecf0f1',
        padding: 8,
    },
    paragraph: {
        margin: 24,
        fontSize: 18,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    center: {
        margin: 24,
        fontSize: 18,
        textAlign: 'center',
        //flex: 1,
    },
});
